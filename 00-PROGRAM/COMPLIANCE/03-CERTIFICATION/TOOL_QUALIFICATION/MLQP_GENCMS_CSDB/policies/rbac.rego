package gencms.authz

# Input shape:
# input.user: { id, roles: [string], groups: [string], clearance: number, audiences: [string] }
# input.object: { type: "DM"|"PM"|"ICN", state: "inWork"|"review"|"approved"|"issue",
#                 audience: [string], classification: number, owner: string,
#                 approvals: [{user: string, groups: [string]}] }
# input.action: "view"|"edit"|"approve"|"publish"|"admin"

default allow := false

# ----- Helpers -----
audience_overlap := some a {
  a := input.object.audience[_]
  input.user.audiences[_] == a
}

has_role[r] { r := input.user.roles[_] }

in_group[g] { g := input.user.groups[_] }

classification_ok := input.user.clearance >= input.object.classification

distinct_approvers := count(distinct_approval_users) >= 2
distinct_approval_users := { a.user | a := input.object.approvals[_] }

# Prevent same user or same primary group approving their own work
not_self_approval := input.user.id != input.object.owner
not_same_primary_group := not same_primary_group()
same_primary_group() {
  some g
  input.user.groups[_] == g
  a := input.object.approvals[_]
  a.groups[_] == g
}

# ----- Role maps -----
# Model roles as capabilities. Extend per program.
role_caps := {
  "Viewer": {"view"},
  "Author": {"view","edit"},
  "Reviewer": {"view","approve"},
  "Publisher": {"view","publish"},
  "Auditor": {"view"},
  "Admin": {"view","edit","approve","publish","admin"},
}

role_allows(action) {
  has_role[r]
  role_caps[r][action]
}

# ----- State gates -----
state_allows("view")    { true }
state_allows("edit")    { input.object.state == "inWork" }
state_allows("approve") { input.object.state == "review" }
state_allows("publish") { input.object.state == "approved" }
state_allows("admin")   { true }

# ----- Decisions -----
allow {
  input.action == "view"
  classification_ok
  audience_overlap
  role_allows("view")
  state_allows("view")
}

allow {
  input.action == "edit"
  classification_ok
  audience_overlap
  role_allows("edit")
  state_allows("edit")
}

allow {
  input.action == "approve"
  classification_ok
  audience_overlap
  role_allows("approve")
  state_allows("approve")
  not_self_approval
  not_same_primary_group
}

allow {
  input.action == "publish"
  classification_ok
  audience_overlap
  role_allows("publish")
  state_allows("publish")
  distinct_approvers
}

allow {
  input.action == "admin"
  role_allows("admin")
}

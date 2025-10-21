import type * as React from "react"
import { cn } from "@/lib/utils"

export interface StatCardProps extends React.HTMLAttributes<HTMLDivElement> {
  label: string
  value: string | number
  icon?: React.ReactNode
}

function StatCard({ className, label, value, icon, ...props }: StatCardProps) {
  return (
    <div className={cn("rounded-lg border bg-slate-50 dark:bg-slate-900/50 p-4 space-y-1", className)} {...props}>
      {icon && <div className="mb-2">{icon}</div>}
      <p className="text-sm text-muted-foreground">{label}</p>
      <p className="text-2xl font-bold">{value}</p>
    </div>
  )
}

export { StatCard }

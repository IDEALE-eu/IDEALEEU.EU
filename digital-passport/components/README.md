# ui — Primitives

Stateless building blocks. TypeScript. Tailwind-only. No data fetching.

## Index
- [alert.tsx](./alert.tsx) — inline status message
- [badge.tsx](./badge.tsx) — small status pill
- [button.tsx](./button.tsx) — actions with variants/sizes
- [dialog.tsx](./dialog.tsx) — modal container
- [input.tsx](./input.tsx) — text input
- [label.tsx](./label.tsx) — form label
- [progress.tsx](./progress.tsx) — linear progress
- [select.tsx](./select.tsx) — single-choice select
- [stat-card.tsx](./stat-card.tsx) — KPI card
- [switch.tsx](./switch.tsx) — toggle
- [tooltip.tsx](./tooltip.tsx) — hover/focus hint

## Conventions
- One component per file. Default export.
- Props typed. No `any`.
- A11y first: roles, aria-*, focus rings.
- Variants via props; compose classes with `cn` from `@/lib/utils`.

## Quick use
```tsx
import Button from "@/components/ui/button";
import Badge from "@/components/ui/badge";
import Tooltip from "@/components/ui/tooltip";

export default function Example() {
  return (
    <div className="space-x-2">
      <Button variant="default">Save</Button>
      <Badge>Verified</Badge>
      <Tooltip content="Open settings">
        <Button aria-label="Settings" variant="ghost">⚙️</Button>
      </Tooltip>
    </div>
  );
}
````

## Barrel export (optional)

```ts
// components/ui/index.ts
export { default as Alert } from "./alert";
export { default as Badge } from "./badge";
export { default as Button } from "./button";
export { default as Dialog } from "./dialog";
export { default as Input } from "./input";
export { default as Label } from "./label";
export { default as Progress } from "./progress";
export { default as Select } from "./select";
export { default as StatCard } from "./stat-card";
export { default as Switch } from "./switch";
export { default as Tooltip } from "./tooltip";
```

## Testing

Use React Testing Library + Vitest. One test per component in `__tests__/`.

```
::contentReference[oaicite:0]{index=0}
```



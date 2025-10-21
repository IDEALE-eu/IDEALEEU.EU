# components/ — UI Components

## Folders
- **ui/** – primitives (Button, Card, Input, Badge)
- **layout/** – AppShell, Navbar, Sidebar, Footer
- **passport/** – Digital Passport widgets (PassportCard, ManifestViewer, StateStepper)
- **tfa/** – TFA domain chips, grid, legend
- **charts/** – lightweight charts (Recharts)
- **icons/** – lucide-react wrappers
- **tables/** – data table, filters, pagination

> Import via aliases (e.g., `@/components/ui/Button`).

## Rules
- React 19 + TypeScript. One component per file. Default export.
- Tailwind only. No inline styles.
- Accessible by default (roles, aria-*, focus rings).
- Pure UI. Fetching and business logic live in `hooks/` or `lib/`.
- Props typed. No `any`. Prefer discriminated unions for variants.

## Naming
- Files: `ComponentName.tsx`
- Tests: `__tests__/ComponentName.test.tsx`
- Stories (optional): `ComponentName.stories.tsx`

## Variants and theming
- Use Tailwind tokens (from `index.css`).
- Expose `variant` and `size` props when useful.
- Compose with class helpers from `@/lib/utils` (e.g., `cn`).

## Example
```tsx
// components/ui/Button.tsx
import { Slot } from "@radix-ui/react-slot";
import { cn } from "@/lib/utils";

type ButtonProps = React.ComponentProps<"button"> & {
  asChild?: boolean;
  variant?: "primary" | "ghost" | "outline";
  size?: "sm" | "md";
};

export default function Button({
  asChild,
  variant = "primary",
  size = "md",
  className,
  ...props
}: ButtonProps) {
  const Comp = asChild ? Slot : "button";
  return (
    <Comp
      className={cn(
        "inline-flex items-center justify-center rounded-2xl font-medium transition-colors",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2",
        size === "sm" ? "px-3 py-1.5 text-sm" : "px-4 py-2 text-sm",
        variant === "primary" && "bg-primary text-white hover:bg-primary/90",
        variant === "ghost" && "hover:bg-neutral-100",
        variant === "outline" && "border border-neutral-300 hover:bg-neutral-50",
        className
      )}
      {...props}
    />
  );
}
````

## Barrel exports

```ts
// components/index.ts
export { default as Button } from "./ui/Button";
export { default as PassportCard } from "./passport/PassportCard";
export { default as ManifestViewer } from "./passport/ManifestViewer";
export { default as DomainChips } from "./tfa/DomainChips";
```

## Lint and tests

```bash
npm run lint
npm run test
```

```
::contentReference[oaicite:0]{index=0}
```


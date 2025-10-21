# ui/ — Primitives

Low-level, reusable UI atoms. Pure presentational components with minimal logic.

## Contents
- **Button.tsx**
- **Card.tsx** (+ `CardHeader`, `CardContent`, `CardFooter`)
- **Input.tsx** (text, number, password)
- **Textarea.tsx**
- **Select.tsx**
- **Badge.tsx**
- **Checkbox.tsx**
- **Switch.tsx**
- **Modal.tsx**
- **Tooltip.tsx**
- **Skeleton.tsx**
- **Tabs.tsx**
- **Alert.tsx**

> Import via alias: `@/components/ui/Button`

## Rules
- TypeScript. Default export per file.
- Tailwind only. No inline styles.
- Accessible by default (aria, roles, focus rings).
- No data fetching. No domain logic.
- Props typed. Avoid `any`. Prefer unions for variants/sizes.

## Patterns
- **Variants:** `variant?: "primary" | "ghost" | "outline"`
- **Sizes:** `size?: "sm" | "md" | "lg"`
- **asChild:** use Radix `Slot` for polymorphic rendering
- **Class merge:** `cn` from `@/lib/utils`

## Example
```tsx
// ui/Button.tsx
import { Slot } from "@radix-ui/react-slot";
import { cn } from "@/lib/utils";

type Props = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  asChild?: boolean;
  variant?: "primary" | "ghost" | "outline";
  size?: "sm" | "md" | "lg";
};

export default function Button({ asChild, variant="primary", size="md", className, ...props }: Props) {
  const Comp = asChild ? Slot : "button";
  return (
    <Comp
      className={cn(
        "inline-flex items-center justify-center rounded-2xl font-medium transition-colors",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2",
        size === "sm" && "px-3 py-1.5 text-sm",
        size === "md" && "px-4 py-2 text-sm",
        size === "lg" && "px-5 py-2.5 text-base",
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

## Testing

* Unit tests in `__tests__/ComponentName.test.tsx`
* Use React Testing Library. Test a11y states and variant classes.

## Checklist

* [ ] Keyboard and screen-reader support
* [ ] Focus visible styles
* [ ] Dark-mode safe colors (Tailwind tokens)
* [ ] Story or MDX snippet for usage

```
::contentReference[oaicite:0]{index=0}
```


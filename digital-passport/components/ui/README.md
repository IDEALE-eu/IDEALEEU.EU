# ui/ — Primitives

Stateless, reusable building blocks. No data fetching. Tailwind-only.

## Available
- **Button** — actions
- **Card** — content container
- **Input** — text input
- **Select** — options
- **Badge** — status label
- **Tooltip** — hints
- **Modal** — dialogs
- **Tabs** — segmented views

Import via alias:
```ts
import Button from "@/components/ui/Button";
````

## Conventions

* One component per file, default export.
* Props are typed. No `any`.
* Accessibility first: roles, aria-*, focus rings.
* Variants via discriminated unions. Sizes: `sm|md|lg`.
* Compose styles with `cn` from `@/lib/utils`.

## Examples

### Button

Improved, accessible, and production-ready Button with loading, full-width, and icon-only a11y.

```tsx
// components/ui/Button.tsx
import React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline: "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9 p-0",
      },
      fullWidth: {
        true: "w-full",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

export interface ButtonProps
  extends Omit<React.ButtonHTMLAttributes<HTMLButtonElement>, "disabled">,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
  /** Show spinner and set aria-busy */
  loading?: boolean;
  /** Disable the button (also when loading) */
  disabled?: boolean;
  /** If the button has only an icon, provide an accessible label */
  "aria-label"?: string;
}

const Spinner = () => (
  <svg
    aria-hidden="true"
    viewBox="0 0 24 24"
    className="h-4 w-4 animate-spin"
  >
    <circle cx="12" cy="12" r="10" stroke="currentColor" strokeOpacity="0.25" fill="none" strokeWidth="4" />
    <path d="M22 12a10 10 0 0 0-10-10" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" />
  </svg>
);

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      className,
      variant,
      size,
      fullWidth,
      asChild = false,
      loading = false,
      disabled,
      type = "button",
      children,
      ...props
    },
    ref
  ) => {
    const Comp: any = asChild ? Slot : "button";
    const isDisabled = disabled || loading;

    return (
      <Comp
        ref={ref}
        type={asChild ? undefined : type}
        className={cn(
          "transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0",
          buttonVariants({ variant, size, fullWidth, className })
        )}
        aria-busy={loading || undefined}
        disabled={isDisabled}
        {...props}
      >
        {loading && <Spinner />}
        {children}
      </Comp>
    );
  }
);
Button.displayName = "Button";

export { Button, buttonVariants };
export type { ButtonProps };
```

Notes:

* Default `type="button"` prevents accidental form submits.
* `loading` sets `aria-busy` and shows a spinner.
* `fullWidth` variant for layout control.
* Icon-only buttons must set `aria-label`.


### Card

```tsx
// ui/Card.tsx
export default function Card({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      className={["rounded-2xl border border-neutral-200 bg-white p-6 shadow-sm", className]
        .filter(Boolean)
        .join(" ")}
      {...props}
    />
  );
}
```

### Input

```tsx
// ui/Input.tsx
type Props = React.ComponentProps<"input"> & { invalid?: boolean };
export default function Input({ className, invalid, ...props }: Props) {
  return (
    <input
      className={[
        "h-9 w-full rounded-xl border px-3 text-sm outline-none",
        invalid ? "border-red-500 focus:ring-red-500" : "border-neutral-300 focus:ring-neutral-400",
        "focus:ring-2",
        className,
      ].join(" ")}
      {...props}
    />
  );
}
```

### Badge

```tsx
// ui/Badge.tsx
type Props = { children: React.ReactNode; color?: "default" | "success" | "warning" | "error" };
export default function Badge({ children, color = "default" }: Props) {
  const map = {
    default: "bg-neutral-100 text-neutral-700",
    success: "bg-green-100 text-green-700",
    warning: "bg-amber-100 text-amber-700",
    error: "bg-red-100 text-red-700",
  } as const;
  return <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs ${map[color]}`}>{children}</span>;
}
```

## Testing

* File: `__tests__/Button.test.tsx`
* Use React Testing Library + Vitest.

## Lint

```bash
npm run lint
```

```
```



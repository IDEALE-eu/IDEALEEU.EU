import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"
import { ChevronDown } from "lucide-react"

const selectVariants = cva(
  "flex h-10 w-full items-center justify-between rounded-lg border bg-white px-3 py-2 text-sm ring-offset-white transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "border-neutral-200 hover:border-neutral-300",
        error: "border-red-500 focus:ring-red-500",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  },
)

export interface SelectProps
  extends React.SelectHTMLAttributes<HTMLSelectElement>,
    VariantProps<typeof selectVariants> {}

const Select = React.forwardRef<HTMLSelectElement, SelectProps>(({ className, variant, children, ...props }, ref) => {
  return (
    <div className="relative">
      <select className={cn(selectVariants({ variant, className }), "appearance-none pr-8")} ref={ref} {...props}>
        {children}
      </select>
      <ChevronDown className="pointer-events-none absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-neutral-500" />
    </div>
  )
})
Select.displayName = "Select"

export { Select, selectVariants }

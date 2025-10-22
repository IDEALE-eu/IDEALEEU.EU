import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const progressVariants = cva("relative h-2 w-full overflow-hidden rounded-full bg-neutral-200", {
  variants: {
    size: {
      sm: "h-1",
      md: "h-2",
      lg: "h-3",
    },
  },
  defaultVariants: {
    size: "md",
  },
})

const progressBarVariants = cva("h-full transition-all duration-300 ease-in-out", {
  variants: {
    variant: {
      default: "bg-blue-600",
      success: "bg-green-600",
      warning: "bg-yellow-600",
      error: "bg-red-600",
    },
  },
  defaultVariants: {
    variant: "default",
  },
})

export interface ProgressProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof progressVariants>,
    VariantProps<typeof progressBarVariants> {
  value?: number
  max?: number
}

const Progress = React.forwardRef<HTMLDivElement, ProgressProps>(
  ({ className, size, variant, value = 0, max = 100, ...props }, ref) => {
    const percentage = Math.min(Math.max((value / max) * 100, 0), 100)

    return (
      <div ref={ref} className={cn(progressVariants({ size, className }))} {...props}>
        <div className={cn(progressBarVariants({ variant }))} style={{ width: `${percentage}%` }} />
      </div>
    )
  },
)
Progress.displayName = "Progress"

export { Progress, progressVariants, progressBarVariants }

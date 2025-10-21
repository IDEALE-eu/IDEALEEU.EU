"use client"

import * as React from "react"
import { cn } from "@/lib/utils"

export interface SwitchProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "type"> {
  onCheckedChange?: (checked: boolean) => void
}

const Switch = React.forwardRef<HTMLInputElement, SwitchProps>(
  ({ className, onCheckedChange, checked, ...props }, ref) => {
    return (
      <label className="relative inline-flex cursor-pointer items-center">
        <input
          type="checkbox"
          className="peer sr-only"
          ref={ref}
          checked={checked}
          onChange={(e) => onCheckedChange?.(e.target.checked)}
          {...props}
        />
        <div
          className={cn(
            "h-6 w-11 rounded-full bg-neutral-200 transition-colors",
            "peer-checked:bg-blue-600",
            "peer-focus:ring-2 peer-focus:ring-blue-500 peer-focus:ring-offset-2",
            "peer-disabled:cursor-not-allowed peer-disabled:opacity-50",
            className,
          )}
        >
          <div
            className={cn(
              "absolute left-0.5 top-0.5 h-5 w-5 rounded-full bg-white shadow-sm transition-transform",
              "peer-checked:translate-x-5",
            )}
          />
        </div>
      </label>
    )
  },
)
Switch.displayName = "Switch"

export { Switch }

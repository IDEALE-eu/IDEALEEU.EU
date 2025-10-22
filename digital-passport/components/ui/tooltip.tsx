"use client"

import * as React from "react"
import { cn } from "@/lib/utils"

export interface TooltipProps extends React.HTMLAttributes<HTMLDivElement> {
  content: React.ReactNode
  side?: "top" | "right" | "bottom" | "left"
}

const Tooltip = React.forwardRef<HTMLDivElement, TooltipProps>(
  ({ className, content, side = "top", children, ...props }, ref) => {
    const [isVisible, setIsVisible] = React.useState(false)

    const sideClasses = {
      top: "bottom-full left-1/2 -translate-x-1/2 mb-2",
      right: "left-full top-1/2 -translate-y-1/2 ml-2",
      bottom: "top-full left-1/2 -translate-x-1/2 mt-2",
      left: "right-full top-1/2 -translate-y-1/2 mr-2",
    }

    return (
      <div
        ref={ref}
        className={cn("relative inline-block", className)}
        onMouseEnter={() => setIsVisible(true)}
        onMouseLeave={() => setIsVisible(false)}
        {...props}
      >
        {children}
        {isVisible && (
          <div
            className={cn(
              "absolute z-50 rounded-lg bg-neutral-900 px-3 py-2 text-sm text-white shadow-lg",
              "animate-in fade-in-0 zoom-in-95",
              sideClasses[side],
            )}
          >
            {content}
            <div
              className={cn(
                "absolute h-2 w-2 rotate-45 bg-neutral-900",
                side === "top" && "bottom-[-4px] left-1/2 -translate-x-1/2",
                side === "right" && "left-[-4px] top-1/2 -translate-y-1/2",
                side === "bottom" && "top-[-4px] left-1/2 -translate-x-1/2",
                side === "left" && "right-[-4px] top-1/2 -translate-y-1/2",
              )}
            />
          </div>
        )}
      </div>
    )
  },
)
Tooltip.displayName = "Tooltip"

export { Tooltip }

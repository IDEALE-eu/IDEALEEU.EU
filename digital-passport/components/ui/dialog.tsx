"use client"

import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"
import { X } from "lucide-react"

const dialogVariants = cva(
  "fixed left-1/2 top-1/2 z-50 w-full max-w-lg -translate-x-1/2 -translate-y-1/2 rounded-2xl border border-neutral-200 bg-white p-6 shadow-2xl",
  {
    variants: {
      size: {
        sm: "max-w-sm",
        md: "max-w-lg",
        lg: "max-w-2xl",
        xl: "max-w-4xl",
      },
    },
    defaultVariants: {
      size: "md",
    },
  },
)

export interface DialogProps extends React.HTMLAttributes<HTMLDivElement>, VariantProps<typeof dialogVariants> {
  open?: boolean
  onOpenChange?: (open: boolean) => void
}

const Dialog = React.forwardRef<HTMLDivElement, DialogProps>(
  ({ className, size, open, onOpenChange, children, ...props }, ref) => {
    React.useEffect(() => {
      if (open) {
        document.body.style.overflow = "hidden"
      } else {
        document.body.style.overflow = "unset"
      }
      return () => {
        document.body.style.overflow = "unset"
      }
    }, [open])

    if (!open) return null

    return (
      <>
        {/* Backdrop */}
        <div
          className="fixed inset-0 z-40 bg-black/50 backdrop-blur-sm animate-in fade-in-0"
          onClick={() => onOpenChange?.(false)}
        />
        {/* Dialog */}
        <div
          ref={ref}
          className={cn(dialogVariants({ size, className }), "animate-in fade-in-0 zoom-in-95")}
          {...props}
        >
          <button
            onClick={() => onOpenChange?.(false)}
            className="absolute right-4 top-4 rounded-lg p-1 text-neutral-500 hover:bg-neutral-100 hover:text-neutral-900 transition-colors"
          >
            <X className="h-5 w-5" />
          </button>
          {children}
        </div>
      </>
    )
  },
)
Dialog.displayName = "Dialog"

const DialogHeader = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => <div ref={ref} className={cn("mb-4 space-y-1.5", className)} {...props} />,
)
DialogHeader.displayName = "DialogHeader"

const DialogTitle = React.forwardRef<HTMLHeadingElement, React.HTMLAttributes<HTMLHeadingElement>>(
  ({ className, ...props }, ref) => (
    <h2 ref={ref} className={cn("text-2xl font-semibold text-neutral-900", className)} {...props} />
  ),
)
DialogTitle.displayName = "DialogTitle"

const DialogDescription = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(
  ({ className, ...props }, ref) => <p ref={ref} className={cn("text-sm text-neutral-600", className)} {...props} />,
)
DialogDescription.displayName = "DialogDescription"

const DialogFooter = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("mt-6 flex items-center justify-end gap-2", className)} {...props} />
  ),
)
DialogFooter.displayName = "DialogFooter"

export { Dialog, DialogHeader, DialogTitle, DialogDescription, DialogFooter, dialogVariants }

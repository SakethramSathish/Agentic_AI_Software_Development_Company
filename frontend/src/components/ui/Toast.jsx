import { useState, useEffect, createContext, useContext, useCallback } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { X, CheckCircle, AlertTriangle, Info } from 'lucide-react'

const ToastContext = createContext()

const ICONS = {
  success: <CheckCircle size={18} />,
  error: <AlertTriangle size={18} />,
  info: <Info size={18} />,
}

const COLORS = {
  success: 'bg-brutal-green text-black',
  error: 'bg-brutal-red text-white',
  info: 'bg-brutal-blue text-black',
}

export function ToastProvider({ children }) {
  const [toasts, setToasts] = useState([])

  const addToast = useCallback((message, type = 'info', duration = 4000) => {
    const id = Date.now()
    setToasts(prev => [...prev, { id, message, type }])
    setTimeout(() => {
      setToasts(prev => prev.filter(t => t.id !== id))
    }, duration)
  }, [])

  const removeToast = useCallback((id) => {
    setToasts(prev => prev.filter(t => t.id !== id))
  }, [])

  return (
    <ToastContext.Provider value={{ addToast }}>
      {children}

      {/* Toast container */}
      <div className="fixed top-4 right-4 z-50 flex flex-col gap-3 max-w-sm">
        <AnimatePresence>
          {toasts.map(toast => (
            <motion.div
              key={toast.id}
              initial={{ x: 100, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              exit={{ x: 100, opacity: 0 }}
              className={`brutal-card p-4 flex items-start gap-3 ${COLORS[toast.type]}`}
              style={{ boxShadow: '4px 4px 0px 0px var(--shadow-color)' }}
            >
              {ICONS[toast.type]}
              <p className="font-body text-sm font-medium flex-1">{toast.message}</p>
              <button onClick={() => removeToast(toast.id)} className="hover:opacity-70">
                <X size={16} />
              </button>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>
    </ToastContext.Provider>
  )
}

export function useToast() {
  const ctx = useContext(ToastContext)
  if (!ctx) throw new Error('useToast must be used within ToastProvider')
  return ctx
}

import { motion } from 'framer-motion'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { FileText } from 'lucide-react'

/**
 * Final project documentation display.
 */
export default function ResultsSummary({ finalSummary }) {
  if (!finalSummary) return null

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="brutal-card overflow-hidden"
    >
      {/* Header */}
      <div className="bg-brutal-green text-black px-5 py-4 flex items-center gap-3 border-b-[3px] border-[var(--border-color)]">
        <FileText size={22} />
        <h2 className="font-heading text-xl font-extrabold uppercase tracking-wide">
          Final Project Documentation
        </h2>
      </div>

      {/* Content */}
      <div className="p-6 markdown-content" style={{ background: 'var(--bg-card)' }}>
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {finalSummary}
        </ReactMarkdown>
      </div>
    </motion.div>
  )
}

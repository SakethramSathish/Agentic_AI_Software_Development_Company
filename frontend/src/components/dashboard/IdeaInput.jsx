import { useState } from 'react'
import { motion } from 'framer-motion'
import { Rocket, Sparkles } from 'lucide-react'
import Button from '../ui/Button'

const TEMPLATES = [
  'AI-powered study planner for students',
  'E-commerce marketplace with recommendations',
  'Real-time chat app with AI moderation',
  'Health tracker with AI insights',
  'Project management tool with automation',
]

/**
 * Hero section with idea input form and template chips.
 */
export default function IdeaInput({ onSubmit, isRunning }) {
  const [idea, setIdea] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (idea.trim() && !isRunning) {
      onSubmit(idea.trim())
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      {/* Hero Header */}
      <div className="text-center mb-8">
        <motion.h1
          className="font-heading text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight mb-4"
          style={{ color: 'var(--text-primary)' }}
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
        >
          BUILD SOFTWARE
          <br />
          <span className="bg-brutal-yellow text-black px-3 py-1 border-[3px] border-[var(--border-color)] inline-block mt-2"
                style={{ boxShadow: '4px 4px 0px 0px var(--shadow-color)' }}>
            WITH AI AGENTS
          </span>
        </motion.h1>
        <motion.p
          className="font-body text-base max-w-xl mx-auto mt-4"
          style={{ color: 'var(--text-secondary)' }}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
        >
          Describe your idea. 10 AI agents — CEO, PM, Architect, Developers, QA — will
          build it end-to-end, powered by Gemini + LangGraph.
        </motion.p>
      </div>

      {/* Input Form */}
      <form onSubmit={handleSubmit} className="max-w-3xl mx-auto">
        <div className="brutal-card p-6">
          {/* Text Area */}
          <textarea
            id="idea-input"
            value={idea}
            onChange={(e) => setIdea(e.target.value)}
            placeholder="Example: Build an AI-powered study planner for college students with smart scheduling..."
            rows={5}
            disabled={isRunning}
            className="brutal-input w-full p-4 text-base resize-none font-body"
          />

          {/* Character count */}
          <div className="flex items-center justify-between mt-3 mb-4">
            <span className="text-xs font-heading font-bold uppercase" style={{ color: 'var(--text-secondary)' }}>
              {idea.length} chars
            </span>
            {idea.length > 0 && idea.length < 20 && (
              <span className="text-xs font-heading font-bold text-brutal-red uppercase">
                Be more descriptive!
              </span>
            )}
          </div>

          {/* Submit Button */}
          <Button
            type="submit"
            variant="primary"
            size="lg"
            disabled={!idea.trim() || isRunning || idea.length < 10}
            className="w-full text-base"
          >
            {isRunning ? (
              <>
                <Sparkles size={20} className="animate-spin" />
                AI Company is Working...
              </>
            ) : (
              <>
                <Rocket size={20} />
                Build with AI Company
              </>
            )}
          </Button>
        </div>

        {/* Template Chips */}
        <div className="mt-4 flex flex-wrap gap-2 justify-center">
          <span className="text-xs font-heading font-bold uppercase" style={{ color: 'var(--text-secondary)' }}>
            Quick start:
          </span>
          {TEMPLATES.map((template) => (
            <motion.button
              key={template}
              type="button"
              whileHover={{ y: -2 }}
              whileTap={{ y: 1 }}
              onClick={() => setIdea(template)}
              disabled={isRunning}
              className="brutal-badge bg-[var(--bg-card)] hover:bg-brutal-peach text-xs cursor-pointer disabled:opacity-50"
              style={{ color: 'var(--text-primary)' }}
            >
              {template}
            </motion.button>
          ))}
        </div>
      </form>
    </motion.div>
  )
}

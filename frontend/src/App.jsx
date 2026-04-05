import { AnimatePresence, motion } from 'framer-motion'
import Layout from './components/layout/Layout'
import IdeaInput from './components/dashboard/IdeaInput'
import PipelineVisualizer from './components/pipeline/PipelineVisualizer'
import AgentOutputPanel from './components/pipeline/AgentOutputPanel'
import ResultsSummary from './components/dashboard/ResultsSummary'
import AgentDetailsGrid from './components/dashboard/AgentDetailsGrid'
import { ToastProvider, useToast } from './components/ui/Toast'
import { useAgentPipeline } from './hooks/useAgentPipeline'
import { AlertTriangle } from 'lucide-react'

function Dashboard() {
  const {
    agents,
    agentStates,
    isRunning,
    isComplete,
    error,
    selectedAgent,
    setSelectedAgent,
    runPipeline,
    getAgentStatus,
  } = useAgentPipeline()

  const { addToast } = useToast()

  const handleSubmit = async (idea) => {
    addToast('Pipeline started! Watch the agents work...', 'info')
    await runPipeline(idea)
  }

  // Get final summary from documentation agent output
  const finalSummary = agentStates['documentation']?.output || ''

  return (
    <Layout>
      <div className="space-y-8">
        {/* Hero + Idea Input */}
        <IdeaInput onSubmit={handleSubmit} isRunning={isRunning} />

        {/* Pipeline Visualizer — only visible when running or complete */}
        <AnimatePresence>
          {(isRunning || isComplete || error) && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              transition={{ duration: 0.4 }}
            >
              <PipelineVisualizer
                agents={agents}
                getAgentStatus={getAgentStatus}
                selectedAgent={selectedAgent}
                onSelectAgent={setSelectedAgent}
              />
            </motion.div>
          )}
        </AnimatePresence>

        {/* Error Display */}
        <AnimatePresence>
          {error && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              className="brutal-card bg-brutal-red text-white p-5 flex items-start gap-3"
            >
              <AlertTriangle size={20} />
              <div>
                <h3 className="font-heading text-sm font-bold uppercase">Pipeline Error</h3>
                <p className="font-body text-sm mt-1">{error}</p>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Selected Agent Output Panel */}
        <AnimatePresence>
          {selectedAgent && agentStates[selectedAgent] && (
            <AgentOutputPanel
              agentKey={selectedAgent}
              output={agentStates[selectedAgent].output}
              onClose={() => setSelectedAgent(null)}
            />
          )}
        </AnimatePresence>

        {/* Final Documentation */}
        {isComplete && finalSummary && (
          <ResultsSummary finalSummary={finalSummary} />
        )}

        {/* Agent Details Grid */}
        {(isRunning || isComplete) && (
          <AgentDetailsGrid
            agentStates={agentStates}
            onSelectAgent={setSelectedAgent}
          />
        )}
      </div>
    </Layout>
  )
}

export default function App() {
  return (
    <ToastProvider>
      <Dashboard />
    </ToastProvider>
  )
}

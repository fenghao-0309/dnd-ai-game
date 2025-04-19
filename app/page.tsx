import DnDGameUI from "@/components/DnDGameUI";
import AuthForm from '@/components/AuthForm'

export default function HomePage() {
  return <DnDGameUI />;
}

export default function Home() {
  return (
    <main className="p-6 max-w-md mx-auto">
      <h1 className="text-xl font-bold mb-4">Login or Sign Up</h1>
      <AuthForm />
    </main>
  )
}

import ProtectedGame from '@/components/ProtectedGame'

export default function Home() {
  return (
    <main className="p-6 max-w-xl mx-auto">
      <ProtectedGame />
    </main>
  )
}
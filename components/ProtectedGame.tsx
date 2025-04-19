'use client'

import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'
import DnDGameUI from './DnDGameUI'
import AuthForm from './AuthForm'

export default function ProtectedGame() {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const getSession = async () => {
      const { data: { session } } = await supabase.auth.getSession()
      setUser(session?.user ?? null)
      setLoading(false)
    }

    getSession()

    const { data: listener } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null)
    })

    return () => {
      listener.subscription.unsubscribe()
    }
  }, [])

  if (loading) return <p>Loading...</p>

  return user ? <DnDGameUI /> : <AuthForm />
}

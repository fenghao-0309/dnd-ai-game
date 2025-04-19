// app/api/game/route.ts
import { NextResponse } from 'next/server'

export async function POST(req: Request) {
  const { input, history } = await req.json()
  const session_id = 'demo-user-session' // you can link this to logged-in user later

  const url = history.length <= 1 ? 'start' : 'play'
  const res = await fetch(`http://localhost:8000/${url}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ session_id, message: input }),
  })

  const data = await res.json()
  return NextResponse.json({ reply: data.reply })
}

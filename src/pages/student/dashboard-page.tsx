import { Link } from "react-router-dom"

import { Button } from "@/components/ui/button"

export function StudentDashboardPage() {
  return (
    <main className="mx-auto flex min-h-screen w-full max-w-4xl flex-col gap-6 p-8">
      <h1 className="text-3xl font-semibold tracking-tight">Student Dashboard</h1>
      <p className="text-muted-foreground">
        Initial scaffold ready. Student features can now be connected to API
        hooks and role-protected routes.
      </p>
      <div>
        <Link to="/dashboard">
          <Button variant="outline">Go to teacher dashboard</Button>
        </Link>
      </div>
    </main>
  )
}

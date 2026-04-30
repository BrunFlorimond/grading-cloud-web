import { Link } from "react-router-dom"

import { Button } from "@/components/ui/button"

export function TeacherDashboardPage() {
  return (
    <main className="mx-auto flex min-h-screen w-full max-w-4xl flex-col gap-6 p-8">
      <h1 className="text-3xl font-semibold tracking-tight">Teacher Dashboard</h1>
      <p className="text-muted-foreground">
        Initial scaffold ready. Teacher routes and feature modules can now be
        implemented incrementally.
      </p>
      <div>
        <Link to="/student/dashboard">
          <Button>Go to student dashboard</Button>
        </Link>
      </div>
    </main>
  )
}

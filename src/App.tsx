import { Navigate, Route, Routes } from "react-router-dom"

import { TeacherDashboardPage } from "@/pages/teacher/dashboard-page"
import { StudentDashboardPage } from "@/pages/student/dashboard-page"

function App() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Routes>
        <Route path="/dashboard" element={<TeacherDashboardPage />} />
        <Route path="/student/dashboard" element={<StudentDashboardPage />} />
        <Route path="*" element={<Navigate replace to="/dashboard" />} />
      </Routes>
    </div>
  )
}

export default App

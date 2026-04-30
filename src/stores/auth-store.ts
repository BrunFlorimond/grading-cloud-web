import { create } from "zustand"

type UserRole = "teacher" | "student" | null

type AuthState = {
  accessToken: string | null
  role: UserRole
  setSession: (accessToken: string, role: Exclude<UserRole, null>) => void
  clearSession: () => void
}

export const useAuthStore = create<AuthState>((set) => ({
  accessToken: null,
  role: null,
  setSession: (accessToken, role) => set({ accessToken, role }),
  clearSession: () => set({ accessToken: null, role: null }),
}))

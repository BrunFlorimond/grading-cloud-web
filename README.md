# grading-cloud-web

Frontend for the [grading-cloud](https://github.com/BrunFlorimond/grading-cloud) pipeline — a React SPA that gives teachers and students a role-scoped interface over the grading API.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | React 18 + Vite + TypeScript |
| UI components | shadcn/ui + Tailwind CSS |
| Server state | TanStack Query v5 (data fetching, polling, mutations) |
| Client state | Zustand (auth token, user role) |
| Auth | @aws-amplify/auth (Cognito token management) |
| API client | orval — generated from FastAPI OpenAPI spec |
| Forms | React Hook Form + Zod |
| Router | React Router v6 |
| Package manager | pnpm |
| Hosting | Amazon S3 + CloudFront (CDK-provisioned in this repo under `infra/`) |

---

## Roles

Two roles, each with a separate navigation scope:

| Role | Entry point | Access |
|---|---|---|
| **Teacher** | `/dashboard` | All exams they created, all students, pipeline controls, rubric builder |
| **Student** | `/student/dashboard` | Their own submission, grade breakdown, PDF download only |

Role is read from the Cognito JWT `custom:role` claim on login. Protected routes redirect to `/login` if unauthenticated, or show a 403 if the role does not match.

---

## Project Structure

```
src/
├── pages/
│   ├── teacher/        # /dashboard, /exams/*, /rubrics/*
│   └── student/        # /student/dashboard, /student/grade
├── components/
│   ├── ui/             # shadcn/ui base components
│   ├── notation/       # NotationTable (shared between teacher and student views)
│   ├── upload/         # UploadZone (shared across all upload flows)
│   └── pipeline/       # StatusBadge, PipelineStepper, ProgressBar
├── hooks/              # Custom hooks wrapping TanStack Query
├── lib/
│   └── api/            # orval-generated typed API client
└── stores/             # Zustand stores (auth)
```

---

## Local Development

```bash
pnpm install
cp .env.example .env.local   # fill in API_URL and Cognito config
pnpm dev
```

Regenerate the typed API client from a running backend:

```bash
pnpm generate-api
```

---

## Deployment

Every merge to `main` triggers a GitHub Actions workflow:

1. `pnpm build` — Vite production build
2. `aws s3 sync dist/ s3://{bucket}` — sync to S3
3. CloudFront invalidation — `/*`

AWS credentials are injected via GitHub OIDC. The S3 bucket and CloudFront distribution are provisioned by `infra/stacks/frontend_stack.py` in this repository.

---

## Roadmap

Developed in parallel vertical slices with the backend — each slice delivers a demoable feature end to end. Backend issues live in [grading-cloud](https://github.com/BrunFlorimond/grading-cloud). Both repos feed into the same project board.

| Slice | What you can demo |
|---|---|
| [Slice 1 – Exam Setup](https://github.com/BrunFlorimond/grading-cloud-web/milestone/1) | Log in as teacher, create an exam, configure it, add students |
| [Slice 2 – Spreadsheet Ingestion](https://github.com/BrunFlorimond/grading-cloud-web/milestone/2) | Upload a spreadsheet, watch it go PENDING → CONVERTED |
| [Slice 3 – AI Correction](https://github.com/BrunFlorimond/grading-cloud-web/milestone/3) | Start grading, watch corrections appear student by student, open a notation breakdown |
| [Slice 4 – Full Pipeline](https://github.com/BrunFlorimond/grading-cloud-web/milestone/4) | End-to-end: spreadsheet in, graded PDF out, downloadable |
| [Slice 5 – Student Portal](https://github.com/BrunFlorimond/grading-cloud-web/milestone/5) | Log in as student, view your grade, download your PDF |
| [Slice 6 – Rubric Builder](https://github.com/BrunFlorimond/grading-cloud-web/milestone/6) | Generate a rubric from an xlsx assignment with Claude, tweak it, attach to an exam |

Full board: [Grading Cloud – Roadmap](https://github.com/users/BrunFlorimond/projects/2)

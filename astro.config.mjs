import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://biginformatics.github.io',
  base: '/git-basics',
  integrations: [
    starlight({
      title: 'Git Basics',
      description: 'Hands-on Git and GitHub lessons for analysts and statisticians.',
      social: [
        {
          icon: 'github',
          label: 'GitHub repository',
          href: 'https://github.com/BigInformatics/git-basics',
        },
      ],
      sidebar: [
        { label: 'Start Here', slug: 'index' },
        {
          label: 'Lessons',
          items: [
            { label: '01 — What Git and GitHub Are', slug: 'lessons/01-what-git-and-github-are' },
            { label: '02 — Setup and Orientation', slug: 'lessons/02-setup-and-orientation' },
            { label: '03 — Cloning a Repository', slug: 'lessons/03-cloning-a-repository' },
            { label: '04 — Status, Staging, and Commits', slug: 'lessons/04-status-staging-commits' },
            { label: '05 — Pushing and Pulling', slug: 'lessons/05-pushing-and-pulling' },
            { label: '06 — Branching', slug: 'lessons/06-branching' },
            { label: '07 — Pull Requests', slug: 'lessons/07-pull-requests' },
            { label: '08 — Complete Workflow', slug: 'lessons/08-complete-workflow' },
          ],
        },
        {
          label: 'Practice',
          items: [
            { label: 'Template Repositories', slug: 'practice/template-repositories' },
            { label: 'Practice Checklist', slug: 'exercises/practice-checklist' },
          ],
        },
        {
          label: 'Resources',
          items: [
            { label: 'Command Cheat Sheet', slug: 'resources/command-cheat-sheet' },
            { label: 'Glossary', slug: 'resources/glossary' },
            { label: 'Facilitator Guide', slug: 'resources/facilitator-guide' },
          ],
        },
      ],
    }),
  ],
});

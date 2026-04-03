import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { glob } from "astro/loaders";

const baseSchema = z.object({
  title: z.string(),
  description: z.string(),
  tags: z.array(z.string()).default([]),
  publishedAt: z.coerce.date(),
  updatedAt: z.coerce.date().optional(),
  draft: z.boolean().default(false),
});

const courses = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/courses" }),
  schema: baseSchema.extend({
    duration: z.number(),
    level: z.enum(["unknown", "beginner", "intermediate", "advanced"]),
  }),
});

const quests = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/quests" }),
  schema: baseSchema.extend({
    difficulty: z.enum(["easy", "medium", "hard"]),
    courseSlug: z.string().optional(),
  }),
});

const livecodings = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/livecodings" }),
  schema: baseSchema.extend({
    duration: z.number(),
    objectives: z.array(z.string()),
  }),
});

export const collections = {
  courses,
  quests,
  livecodings,
};

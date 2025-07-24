import { z } from "zod";

const Base = z.object({
    id: z.number(),
    slug: z.string(),
    isActive: z.boolean(),
});

type Base = z.infer<typeof Base>;

const Category = z.object({
    name: z.string(),
});

export type Category = Base & z.infer<typeof Category>;

const Course = z.object({
    name: z.string(),
});

export type Course = Base & z.infer<typeof Course>;

export type Courses = {
    count: number;
    page_size: number;
    results: Pick<Course, "id" | "isActive" | "slug" | "name">[];
};

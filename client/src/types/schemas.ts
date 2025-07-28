type Base = {
    id: number;
    slug: string;
    isActive: boolean;
};

export type Category = Base & {
    name: string;
};

export type Course = Base & {
    name: string;
};

export type Courses = {
    count: number;
    page_size: number;
    results: Pick<Course, "id" | "isActive" | "slug" | "name">[];
};

export type User = Base & {
    username: string;
};

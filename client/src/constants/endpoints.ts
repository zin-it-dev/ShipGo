export const ENDPOINTS = {
    categories: "/categories/",
    courses: (page: number, category: string | null) => {
        const url = new URLSearchParams({ page: page.toString() });
        if (category) url.append("category", category);
        return `/courses/?${url.toString()}`;
    },
    course: (slug: string | undefined) => `/courses/${slug}`,
    token: "/token/",
    refresh: "/token/refresh/",
    current_user: "/users/current-user/",
};

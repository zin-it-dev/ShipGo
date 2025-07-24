import { keepPreviousData, useQuery } from "@tanstack/react-query";

import type { Course, Courses } from "@/libs/types/schemas";
import { fetchCourse, fetchCourseList } from "@/services/course.service";
import { useParams, useSearchParams } from "react-router";

export const useCourses = () => {
    const [searchParams] = useSearchParams();
    const page: number = Number(searchParams.get("page")) || 1;
    const category = searchParams.get("category");

    return useQuery<Courses>({
        queryKey: ["courses", page, category],
        queryFn: () => fetchCourseList(page, category),
        placeholderData: keepPreviousData,
    });
};

export const useCourse = () => {
    const { slug } = useParams();

    return useQuery<Course>({
        queryKey: ["courses", slug],
        queryFn: () => fetchCourse(slug),
        placeholderData: keepPreviousData,
    });
};

import { keepPreviousData, useQuery } from "@tanstack/react-query";
import { useParams, useSearchParams } from "react-router";

import type { Course, Courses } from "@/types/schemas";
import { fetchCourse, fetchCourseList } from "@/services/course.service";

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
  });
};

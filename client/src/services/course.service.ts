import { ENDPOINTS } from "@/constants/endpoints";
import axios from "@/libs/configs/axios";
import type { Course, Courses } from "@/libs/types/schemas";

export const fetchCourseList = async (
    page: number,
    category: string | null
): Promise<Courses> => {
    const response = await axios.get(ENDPOINTS["courses"](page, category));
    return response.data;
};

export const fetchCourse = async (
    slug: string | undefined
): Promise<Course> => {
    const response = await axios.get(ENDPOINTS["course"](slug));
    return response.data;
};

import { ENDPOINTS } from "@/constants/endpoints";
import axios from "@/libs/configs/axios";
import type { Category } from "@/types/schemas";

export const fetchCategories = async (): Promise<Category[]> => {
    const response = await axios.get(ENDPOINTS.categories);
    return response.data;
};

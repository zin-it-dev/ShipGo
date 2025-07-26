import { useQuery } from "@tanstack/react-query";

import { fetchCategories } from "@/services/category.service";
import type { Category } from "@/types/schemas";

export const useCategories = () => {
    return useQuery<Category[]>({
        queryKey: ["categories"],
        queryFn: fetchCategories,
    });
};

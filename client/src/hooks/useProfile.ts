import { useQuery } from "@tanstack/react-query";

import { fetchUser } from "@/services/auth.service";
import type { User } from "@/types/schemas";

export const useProfile = () => {
    return useQuery<User>({
        queryKey: ["user"],
        queryFn: fetchUser,
        retry: false,
    });
};

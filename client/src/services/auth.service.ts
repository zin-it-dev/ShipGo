import type { logInPayload } from "@/libs/validations/schemas";
import axios from "@/libs/configs/axios";
import { ENDPOINTS } from "@/constants/endpoints";

export const fetchToken = async (payload: logInPayload) => {
    const response = await axios.post(ENDPOINTS.token, payload);
    return response.data;
};

export const fetchUser = async () => {
    const response = await axios.get(ENDPOINTS.current_user);
    return response.data;
};

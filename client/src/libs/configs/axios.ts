import { ENDPOINTS } from "@/constants/endpoints";
import axios from "axios";
import { useNavigate } from "react-router";

const instance = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    timeout: 10000,
    headers: {
        "Content-Type": "application/json",
    },
    withCredentials: true,
});

let isRefreshing = false;
let subscribers: (() => void)[] = [];

function onRefreshed() {
    subscribers.forEach((cb) => cb());
    subscribers = [];
}

instance.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        const navigate = useNavigate();

        if (error.response?.status === 401 && !originalRequest._retry) {
            if (isRefreshing) {
                return new Promise((resolve) => {
                    subscribers.push(() => {
                        resolve(instance(originalRequest));
                    });
                });
            }

            originalRequest._retry = true;
            isRefreshing = true;

            try {
                await instance.post(
                    ENDPOINTS.refresh,
                    {},
                    { withCredentials: true }
                );
                isRefreshing = false;
                onRefreshed();

                return instance(originalRequest);
            } catch (err) {
                isRefreshing = false;
                navigate("/login");
                return Promise.reject(err);
            }
        }
        return Promise.reject(error);
    }
);

export default instance;

import React from "react";
import { useForm, type SubmitHandler } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useNavigate } from "react-router";

import { logInSchema, type logInPayload } from "@/libs/validations/schemas";
import { useMutation } from "@tanstack/react-query";
import { fetchToken } from "@/services/auth.service";

const Login: React.FC = () => {
    const { register, handleSubmit } = useForm<logInPayload>({
        resolver: zodResolver(logInSchema),
    });
    const navigate = useNavigate();

    const mutation = useMutation({
        mutationFn: fetchToken,
        onSuccess: async () => {
            navigate("/");
        },
    });

    const onSubmit: SubmitHandler<logInPayload> = (data) => {
        console.log(data);
        mutation.mutate(data);
    };

    return (
        <div>
            <h1>Log In</h1>

            <form onSubmit={handleSubmit(onSubmit)}>
                <input {...register("email")} />
                <input {...register("password")} />
                <input type="submit" />
            </form>
        </div>
    );
};

export default Login;

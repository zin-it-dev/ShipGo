import { z } from "zod";

export const logInSchema = z.object({
    email: z.string().email(),
    password: z.string(),
});

export type logInPayload = z.infer<typeof logInSchema>;

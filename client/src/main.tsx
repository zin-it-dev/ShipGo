import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router";

import "@/styles/globals.css";
import App from "@/App";
import QueryProvider from "@/providers/query-provider";

const root = document.getElementById("root") as HTMLElement;

createRoot(root!).render(
    <StrictMode>
        <BrowserRouter>
            <QueryProvider>
                <App />
            </QueryProvider>
        </BrowserRouter>
    </StrictMode>
);

import React from "react";
import { Route, Routes } from "react-router";

import Home from "@/pages/Home";
import Details from "@/pages/Details";
import RootLayout from "@/components/layouts/RootLayout";
import Login from "@/pages/Login";

const App: React.FC = () => {
    return (
        <Routes>
            <Route element={<RootLayout />}>
                <Route path="/" element={<Home />} />
                <Route path="/courses/:slug" element={<Details />} />
            </Route>

            <Route path="/login" element={<Login />} />
        </Routes>
    );
};

export default App;

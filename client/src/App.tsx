import React from "react";
import { Route, Routes } from "react-router";

import Home from "@/pages/Home";
import Details from "@/pages/Details";
import RootLayout from "@/components/layouts/RootLayout";

const App: React.FC = () => {
    return (
        <Routes>
            <Route element={<RootLayout />}>
                <Route path="/" element={<Home />} />
                <Route path="/courses/:slug" element={<Details />} />
            </Route>
        </Routes>
    );
};

export default App;

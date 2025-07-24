import React from "react";
import { Outlet } from "react-router";

import Header from "../ui/Header";

const RootLayout: React.FC = () => {
    return (
        <>
            <Header />
            <main>
                <Outlet />
            </main>
        </>
    );
};

export default RootLayout;

import React from "react";

import { useCourse } from "@/hooks/useCourses";

const Details: React.FC = () => {
    const { data, isLoading } = useCourse();

    return (
        <>
            {isLoading ? (
                <p>Loading...</p>
            ) : (
                <div>
                    <h1>{data?.name}</h1>
                    <p></p>
                </div>
            )}
        </>
    );
};

export default Details;

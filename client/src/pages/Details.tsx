import React from "react";

import { useCourse } from "@/hooks/useCourses";

const Details: React.FC = () => {
  const { data, isLoading } = useCourse();

  return (
    <>
      {isLoading ? (
        <p>Loading...</p>
      ) : data ? (
        <div>
          <h1>{data.name}</h1>
          <p>{data.slug}</p>
        </div>
      ) : (
        <p>Not found</p>
      )}
    </>
  );
};

export default Details;

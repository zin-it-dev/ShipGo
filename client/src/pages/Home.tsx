import React from "react";
import { Link } from "react-router";

import { useCourses } from "@/hooks/useCourses";

const Home: React.FC = () => {
  const { data, isLoading } = useCourses();

  const total = data ? Math.ceil(data.count / data.page_size) : 1;

  return (
    <div>
      <h1>Welcome to EdTech !!!</h1>

      {isLoading ? (
        <p>Loading...</p>
      ) : data && data.results.length > 0 ? (
        <>
          <ul>
            {data?.results.map((course) => (
              <li key={course.id}>
                <Link to={`/courses/${course.slug}`}>{course.name}</Link>
              </li>
            ))}
          </ul>

          <ul>
            {Array.from({ length: total }, (_, idx) => (
              <li key={idx + 1}>
                <Link to={`/?page=${idx + 1}`}>{idx + 1}</Link>
              </li>
            ))}
          </ul>
        </>
      ) : (
        <p>Not found data</p>
      )}
    </div>
  );
};

export default Home;

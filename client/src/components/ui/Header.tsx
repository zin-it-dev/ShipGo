import React from "react";

import { useCategories } from "@/hooks/useCategories";
import { Link } from "react-router";

const Header: React.FC = () => {
  const { data, isLoading } = useCategories();

  return (
    <header>
      {!isLoading && data && data.length > 0 && (
        <ul>
          {data.map((category) => (
            <li key={category.id}>
              <Link to={`/?category=${category.slug}`}>{category.name}</Link>
            </li>
          ))}
        </ul>
      )}
    </header>
  );
};

export default Header;

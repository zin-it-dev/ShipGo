import { Stack } from "expo-router";

import QueryProvider from "@/providers/query-provider";

export default function RootLayout() {
  return (
    <QueryProvider>
      <Stack
        screenOptions={{
          headerStyle: { backgroundColor: "#fff" },
          headerTintColor: "#000",
        }}
      />
    </QueryProvider>
  );
}

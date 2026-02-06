import "./globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "Project Chimera",
  description: "Chimera frontend",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

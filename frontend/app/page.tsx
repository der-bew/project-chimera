"use client";

import { useEffect, useState } from "react";

type HealthResponse = {
  status: string;
};

export default function HomePage() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const baseUrl = process.env.NEXT_PUBLIC_API_BASE ?? "http://localhost:8000";
    const url = `${baseUrl}/health`;

    fetch(url)
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Health check failed: ${res.status}`);
        }
        return res.json() as Promise<HealthResponse>;
      })
      .then(setHealth)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <main className="page">
      <section className="card">
        <h1>Project Chimera</h1>
        <p>Frontend is running. Backend health:</p>
        {error ? (
          <p className="error">{error}</p>
        ) : health ? (
          <p className="status">{health.status}</p>
        ) : (
          <p className="status">checking...</p>
        )}
      </section>
    </main>
  );
}

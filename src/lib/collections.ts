export const COLLECTIONS = {
  courses: { label: "Cours", href: "/courses" },
  quests: { label: "Quêtes", href: "/quests" },
  livecodings: { label: "Livecoding", href: "/livecodings" },
} as const;

export type CollectionKey = keyof typeof COLLECTIONS;

export function getMeta(entry: {
  collection: CollectionKey;
  data: Record<string, unknown>;
}): string {
  const label = COLLECTIONS[entry.collection].label;
  if (entry.collection === "courses") {
    const d = entry.data as { level: string; duration: number };
    return `${label} · ${d.level} · ${d.duration} min`;
  }
  if (entry.collection === "quests") {
    const d = entry.data as { difficulty: string };
    return `${label} · ${d.difficulty}`;
  }
  if (entry.collection === "livecodings") {
    const d = entry.data as { duration: number };
    return `${label} · ${d.duration} min`;
  }
  return label;
}

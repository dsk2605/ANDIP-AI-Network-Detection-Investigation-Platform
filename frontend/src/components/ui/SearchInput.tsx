import { Search } from "lucide-react";

interface Props {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
}

export default function SearchInput({
  value,
  onChange,
  placeholder = "Search...",
}: Props) {
  return (
    <div className="relative w-full max-w-sm">

      <Search
        size={18}
        className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500"
      />

      <input
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className="
          w-full
          rounded-lg
          border
          border-slate-700
          bg-slate-950
          py-2.5
          pl-10
          pr-4
          text-sm
          text-white
          outline-none
          transition
          focus:border-cyan-500
        "
      />

    </div>
  );
}
interface Props {
  title: string;
  subtitle?: string;
}

export default function TableHeader({
  title,
  subtitle,
}: Props) {
  return (
    <div className="flex items-center justify-between border-b border-slate-800 px-6 py-5">

      <div>

        <h2 className="text-lg font-semibold text-white">
          {title}
        </h2>

        {subtitle && (
          <p className="mt-1 text-sm text-slate-400">
            {subtitle}
          </p>
        )}

      </div>

    </div>
  );
}
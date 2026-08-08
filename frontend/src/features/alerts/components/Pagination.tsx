interface Props {
  page: number;
  pages: number;

  onPrevious: () => void;
  onNext: () => void;
}

export default function Pagination({
  page,
  pages,
  onPrevious,
  onNext,
}: Props) {
  return (
    <div className="flex items-center justify-between rounded-xl border border-slate-800 bg-slate-900 p-4">

      <button
        onClick={onPrevious}
        disabled={page === 1}
        className="rounded-lg border border-slate-700 px-4 py-2 disabled:opacity-40"
      >
        Previous
      </button>

      <span className="text-sm text-slate-400">
        Page {page} of {pages}
      </span>

      <button
        onClick={onNext}
        disabled={page === pages}
        className="rounded-lg border border-slate-700 px-4 py-2 disabled:opacity-40"
      >
        Next
      </button>

    </div>
  );
}
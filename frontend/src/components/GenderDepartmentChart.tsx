"use client"

import { PieChart, Pie, Cell, ResponsiveContainer } from "recharts"
import { useMemo, memo, useCallback } from "react"

const data = [
  { name: "분류 1", value: 928, color: "#8A2BE2" },
  { name: "분류 2", value: 592, color: "#9370DB" },
  { name: "분류 3", value: 428, color: "#BA55D3" },
  { name: "분류 4", value: 412, color: "#DDA0DD" },
  { name: "분류 5", value: 266, color: "#EE82EE" },
  { name: "기타", value: 122, color: "#E6E6FA" },
]

interface GenderDepartmentChartProps {
  onCategorySelect: (category: string) => void
  selectedCategory: string | null
}

// 컴포넌트를 memo로 감싸서 불필요한 리렌더링 방지
const GenderDepartmentChart = memo(({ onCategorySelect, selectedCategory }: GenderDepartmentChartProps) => {
  // 총 개수 계산을 useMemo로 최적화
  const totalCount = useMemo(() => data.reduce((sum, item) => sum + item.value, 0), [])

  // 클릭 핸들러를 useCallback으로 최적화
  const handleClick = useCallback(
    (entry: { name: string }) => {
      onCategorySelect(entry.name)
    },
    [onCategorySelect],
  )

  // 커스텀 라벨 렌더링 함수를 useMemo로 최적화
  const renderCustomizedLabel = useCallback(
    ({
      cx,
      cy,
      midAngle,
      // innerRadius,
      outerRadius,
      index,
      name,
      value,
    }: {
      cx: number
      cy: number
      midAngle: number
      innerRadius: number
      outerRadius: number
      index: number
      name: string
      value: number
    }) => {
      const RADIAN = Math.PI / 180
      // radius 변수는 사용되지 않으므로 제거
      const sin = Math.sin(-midAngle * RADIAN)
      const cos = Math.cos(-midAngle * RADIAN)
      const sx = cx + (outerRadius + 10) * cos
      const sy = cy + (outerRadius + 10) * sin
      const mx = cx + (outerRadius + 30) * cos
      const my = cy + (outerRadius + 30) * sin
      const ex = mx + (cos >= 0 ? 1 : -1) * 22
      const ey = my

      const textAnchor = cos >= 0 ? "start" : "end"

      return (
        <g>
          <text x={cx} y={cy} dy={8} textAnchor="middle" fill="#333" fontSize={20}>
            {totalCount}
          </text>
          <path d={`M${sx},${sy}L${mx},${my}L${ex},${ey}`} stroke={data[index].color} fill="none" />
          <circle cx={ex} cy={ey} r={2} fill={data[index].color} stroke="none" />
          <text
            x={ex + (cos >= 0 ? 1 : -1) * 12}
            y={ey}
            textAnchor={textAnchor}
            fill="#333"
            fontSize={14}
            dominantBaseline="central"
            style={{ cursor: "pointer", fontWeight: selectedCategory === name ? "bold" : "normal" }}
            onClick={() => handleClick(data[index])}
          >
            {name}
          </text>
          <text
            x={ex + (cos >= 0 ? 1 : -1) * 12}
            y={ey + 20}
            textAnchor={textAnchor}
            fill="#666"
            fontSize={12}
            dominantBaseline="central"
          >
            {value}
          </text>
        </g>
      )
    },
    [selectedCategory, handleClick, totalCount],
  )

  // 셀 데이터를 useMemo로 최적화
  const cellData = useMemo(
    () =>
      data.map((entry, index) => (
        <Cell
          key={`cell-${index}`}
          fill={entry.color}
          opacity={selectedCategory === null || selectedCategory === entry.name ? 1 : 0.5}
        />
      )),
    [selectedCategory],
  )

  return (
    <div className="pt-2 px-4 flex justify-center">
      <div className="w-full max-w-2xl">
        <h2 className="text-2xl font-bold text-center mb-4 text-[#8A2BE2]">여성가족부</h2>
        <ResponsiveContainer width="100%" height={550}>
          <PieChart>
            <Pie
              data={data}
              cx="50%"
              cy="50%"
              innerRadius={120}
              outerRadius={190}
              fill="#8884d8"
              paddingAngle={1}
              dataKey="value"
              labelLine={false}
              label={renderCustomizedLabel}
              onClick={(entry) => handleClick(entry)}
              cursor="pointer"
            >
              {cellData}
            </Pie>
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
})

// 컴포넌트 표시 이름 설정
GenderDepartmentChart.displayName = "GenderDepartmentChart"

export default GenderDepartmentChart


-- 코드를 입력하세요
SELECT p.member_name 멤버명, r.review_text 리뷰, DATE_FORMAT(r.review_date, '%Y-%m-%d') 리뷰작성일
FROM member_profile p, rest_review r
WHERE p.member_id = r.member_id
      AND p.member_id = (SELECT r.member_id
                        FROM rest_review r
                        GROUP BY r.member_id
                        ORDER BY COUNT(*) DESC
                        LIMIT 1)
ORDER BY 리뷰작성일, 리뷰;